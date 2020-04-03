from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from team_manager.models import Member
import json
from datetime import datetime


class ManageTeam(APIView):
    """
    This Contracts Dashboard API fetches Contracts data from supplied Excel Sheet / Fetches existing data from DB
    """
    def get(self, request):

        member_data = Member.manager.get_all_member_details()
        message =  "Member data fetched from DB."
        response = {'message': message, 'member_data': member_data}
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        data = json.loads(request.body)
        time_now = datetime.now()
        print(data)
        data['created_at'] = time_now
        member_obj = Member.manager.add_team_member(**data)
        message =  f"Member {member_obj} created. Data stored in DB."
        response = {'message': message}
        return Response(response, status=status.HTTP_201_CREATED)
    #
    def put(self, request):
        data = json.loads(request.body)
        time_now = datetime.now()
        data['updated_at'] = time_now
        member_obj = Member.manager.edit_team_member(**data)
        if member_obj in ['Object Not Found']:
            message = f"Member Not Found"
            response = {'message': message}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        else:
            message = f"Member {member_obj} updated. Data stored in DB."
            response = {'message': message}
            return Response(response, status=status.HTTP_200_OK)

    def delete(self, request):
        member_id = json.loads(request.body).get('member_id')
        member_obj = Member.manager.delete_team_member(member_id)
        message = f'Member {member_obj} deleted'
        response = {'message': message}
        return Response(response, status=status.HTTP_200_OK)