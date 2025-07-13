import os
import ast  # For parsing dict from text file
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

# Step 1: Set your Groq API key
os.environ["GROQ_API_KEY"] = "yourapi"

# Step 2: Load and parse spaCy output from file
with open("output/processed_output.txt", "r") as f:
    content = f.read()
    extracted = ast.literal_eval(content)

# Step 3: Generate summary string for LLM
doc_map = extracted["documents_present"]
summary = f"""
Seller: {extracted["names"][1] if len(extracted["names"]) > 1 else "Unknown"}
Buyer: {extracted["names"][2] if len(extracted["names"]) > 2 else "Unknown"}
Amount: {extracted["transaction_amount"]}
Address: {extracted["property_address"] or "Not found"}

Documents Present:
- Sale Deed: {'✅' if doc_map['sale_deed'] else '❌'}
- EC: {'✅' if doc_map['ec'] else '❌'}
- Possession Letter: {'✅' if doc_map['possession_letter'] else '❌'}
- Title Deed: {'✅' if doc_map['title_deed'] else '❌'}
- Mutation Certificate: {'✅' if doc_map['mutation_certificate'] else '❌'}
- Tax Receipt: {'✅' if doc_map['tax_receipt'] else '❌'}
- RERA Certificate: {'✅' if doc_map['rera_certificate'] else '❌'}
- Power of Attorney: {'✅' if doc_map['power_of_attorney'] else '❌'}
- ID Proof: {'✅' if doc_map['id_proof'] else '❌'}
- Approved Building Plan: {'✅' if doc_map['building_plan'] else '❌'}
"""

# Step 4: Define prompt template
prompt = PromptTemplate(
    input_variables=["summary"],
    template="""
You are an AI legal assistant helping a buyer evaluate if a property is safe to purchase.

Here are the extracted details:
{summary}

Based on Indian property documentation rules, answer:
1. Is the property safe to buy? (Safe or Unsafe)
2. Why?

Be concise and accurate.
"""
)

# Step 5: Setup LangChain with Groq
llm = ChatGroq(model="llama3-8b-8192", temperature=0)
chain: RunnableSequence = prompt | llm

# Step 6: Run inference
result = chain.invoke({"summary": summary})
print("\n Verdict:\n", result.content)
