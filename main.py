from fastapi import FastAPI
from pydantic import BaseModel
from llm_handler import handle_llm
from salesforce_api import get_salesforce_data
from baan_api import get_baan_data
from modeln_api import get_modeln_data



app = FastAPI()

# Define expected request structure
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    user_message = request.message

    # You can now process this input
    sf_data = get_salesforce_data(user_message)
    #response = handle_llm(user_message)
    baan_data = get_baan_data()
    modeln_data = get_modeln_data()

    context = f"""
    Salesforce says: {sf_data}
    BAAN says: {baan_data}
    Model N says: {modeln_data}
    """

    response = handle_llm(user_message)




    return {"response": response}
