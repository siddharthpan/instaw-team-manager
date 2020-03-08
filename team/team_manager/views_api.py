from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status

class ManageTeam(APIView):
    """
    This Contracts Dashboard API fetches Contracts data from supplied Excel Sheet / Fetches existing data from DB
    """
    def get(self, request):
        inventory_data = Contract.manager.get_contract_values()
        message =  "Inventory data fetched from DB."
        response = {'message': message, 'inv_data': inventory_data}
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        get_contracts_data_async()
        message =  "Contracts data fetched. Data stored in DB."
        response = {'message': message}
        return Response(response, status=status.HTTP_201_CREATED)

    def put(self, request):
        inventory_data = Contract.manager.get_contract_values()
        message =  "Inventory data fetched from DB."
        response = {'message': message, 'inv_data': inventory_data}
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request):
        response = {'message': message, 'inv_data': inventory_data}
        return Response(response, status=status.HTTP_200_OK)