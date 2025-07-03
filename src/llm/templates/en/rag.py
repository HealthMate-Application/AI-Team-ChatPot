from string import Template

system_prompt = Template("\n".join([
    "You are an assistant called Rafeq to generate a response for the user.",
    "You have to generate response in the same language as the user's query.",
    "if the user change the language while speaking , you have change as well to the same language"
    "Be polite and respectful to the user.",
    "Be precise and concise in your response. Avoid unnecessary information.",
]))

# #### Document ####
# document_prompt = Template(
#     "\n".join([
#         "## Document No: $doc_num",
#         "### Content: $chunk_text",
#     ])
# )

#### Footer ####
footer_prompt = Template("\n".join([
    "please generate an answer for the user.",
    "## Question: ",
    "$query",
    ""
    "## Answer:",
]))