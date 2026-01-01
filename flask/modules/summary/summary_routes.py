from flask import Blueprint, request, jsonify
from modules.summary.summary_service import SummaryService
from modules.summary.summary_dto import SummarizeDTO
from integrations.openai_client import OpenAIClient

summary_routes = Blueprint('summary_routes', __name__,url_prefix='/api/summary')

@summary_routes.route('', methods=['POST'])
def summarize():
    file = SummarizeDTO.from_request(request.files.get('file'))
    
    ai_client = OpenAIClient()
    service = SummaryService(ai_client)

    summary = service.summarize(file)
    return jsonify(summary.to_dict())