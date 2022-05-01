from pydantic import BaseModel

class ContractCall(BaseModel):
    methodName: str
    params: dict[str,str]
    contractAddress: str
    
class Event(BaseModel):
    status: str
    counterparty: str
    contractCall: ContractCall