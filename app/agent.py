from app.llm import llm_with_tools
from app.tools import (
    create_it_ticket,
    check_ticket_status,
    calculate_expense,
    search_knowledge_base,
)


tools = {
    "create_it_ticket": create_it_ticket,
    "check_ticket_status": check_ticket_status,
    "calculate_expense": calculate_expense,
    "search_knowledge_base": search_knowledge_base,
}


def run_agent(user_input: str) -> str:
    response = llm_with_tools.invoke(user_input)

    if not response.tool_calls:
        return response.content

    tool_results = []
    action_tool_called = False

    for tool_call in response.tool_calls:
        tool_name = tool_call["name"]
        tool = tools.get(tool_name)

        if not tool:
            tool_results.append(
                f"Tool: {tool_name}\n"
                f"Result: Tool not available."
            )
            continue

        result = tool.invoke(tool_call["args"])

        if tool_name in {
            "create_it_ticket",
            "check_ticket_status",
            "calculate_expense",
        }:
            action_tool_called = True

        tool_results.append(
            f"Tool: {tool_name}\n"
            f"Result: {result}"
        )

    if action_tool_called and len(tool_results) == 1:
        return tool_results[0].split("Result: ", 1)[1]

    final_prompt = f"""
You are an enterprise AI operations assistant.

The user asked:
{user_input}

A knowledge-base tool was executed to handle the request.

Tool result:
{chr(10).join(tool_results)}

Respond to the user using the information contained in the tool result.

IMPORTANT:
- Treat information returned by the tool as authoritative.
- Do not claim that information is missing if it is present in the tool result.
- Do not invent information that is not present in the tool result.
- For knowledge-base answers, preserve the factual answer and source information returned by the tool.
- Do not introduce policies, procedures, or facts that are not present in the tool result.
- Give the user a concise, natural-language answer.
"""

    final_response = llm_with_tools.invoke(final_prompt)

    return final_response.content