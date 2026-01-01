from flask import Blueprint, request, jsonify
from modules.task.user_service import TaskService
from utils.time import parse_datetime

task_routes = Blueprint('task_routes', __name__,url_prefix='/api/tasks')

@task_routes.route('', methods=['POST'])
def create_task():
    data = request.get_json()

    startTime = parse_datetime(data.get("startTime"))
    endTime = parse_datetime(data.get("endTime"))

    return jsonify(TaskService.create({
        "name": data.get("name"),
        "startTime": startTime,
        "endTime": endTime
    }).to_dict())


@task_routes.route('', methods=['GET'])
def get_tasks():
    tasks = TaskService.get_all()

    return jsonify([task.to_dict() for task in tasks])
