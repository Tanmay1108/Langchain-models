import json
from tests.t_utils import compare_dict_response

url = "/corp/v1/corporate-users"
corp_user_group_url = "/corp/v1/corporate-user-groups"

def test_create_corp_user(client, data_provider, super_user_token):
    corp_user_data = data_provider.get_data("corp-user")[0]
    response = client.post(url, data=json.dumps(dict(data=corp_user_data)), content_type="application/json", headers=super_user_token)
    response_user = response.json.get("data")
    corp_user_data["isActive"] = True
    corp_user_data["version"] = 1
    assert response.status_code == 200
    assert response_user.get("corpUserId").startswith("CRUS")
    assert response_user.get("userName").get("firstName") == corp_user_data.get("userName").get("firstName")
    compare_dict_response(corp_user_data, response_user, exclude_list=["userName"])


def test_get_corp_user(client, data_provider, super_user_token):
    corp_user_data = data_provider.get_data("corp-user")[0]
    get_url = url + "?corpUserIds=CRUS1"
    response = client.get(get_url, content_type="application/json", headers=super_user_token)
    response_user = response.json.get("data")
    assert response.status_code == 200
    assert response_user[0].get("corpUserId") == "CRUS1"
    assert response_user[0].get("userName").get("firstName") == corp_user_data.get("userName").get("firstName")
    compare_dict_response(corp_user_data, response_user[0], exclude_list=["corpUserId", "userName", "userId", "uniqueHash", "corpUserGroupIds"])


def test_update_corp_user(client, data_provider, super_user_token):
    update_corp_user_data = {
            "phoneNumber": {"countryCode":"+91","number": "9999999991"},
            "userName": {"firstName": "Changedname", "middleName": "test", "lastName": "test lastname"},
            "corpEmail": "admin1@delyvr.in"
        }
    get_url = url + "/CRUS1"
    response = client.patch(
        get_url,
        data=json.dumps(dict(data=update_corp_user_data, resourceVersion=1)), content_type="application/json",
        headers=super_user_token)
    response_user = response.json.get("data")
    assert response.status_code == 200, response.json
    assert response_user.get("corpUserId") == "CRUS1"
    assert response_user.get("userName").get("firstName") == update_corp_user_data.get("userName").get("firstName")
    compare_dict_response(update_corp_user_data, response_user,
                          exclude_list=["corpUserId", "userName", "version", "userId", "uniqueHash", "corpUserGroupIds"]
                          )


def test_create_corp_user_group(client, data_provider, super_user_token):
    corp_user_group_data = data_provider.get_data("corp-user")[1]
    response = client.post(corp_user_group_url, data=json.dumps(dict(data=corp_user_group_data)), content_type="application/json", headers=super_user_token)
    response_user = response.json.get("data")
    assert response.status_code == 200
    assert response_user.get("groupId").startswith("CRUG")
    compare_dict_response(corp_user_group_data, response_user)


def test_get_corp_user_group(client, data_provider, super_user_token):
    corp_user_group_data = data_provider.get_data("corp-user")[1]
    get_url = corp_user_group_url + "?corpUserGroupIds=CRUG1"
    response = client.get(get_url, content_type="application/json", headers=super_user_token)
    response_user = response.json.get("data")
    assert response.status_code == 200
    compare_dict_response(corp_user_group_data, response_user[0])


def test_update_corp_user_group(client, data_provider, super_user_token):
    update_corp_user_group_data = {
            "groupName": "new group name",
            "description": "new test"
        }
    get_url = corp_user_group_url + "/CRUG1"
    response = client.patch(
        get_url,
        data=json.dumps(dict(data=update_corp_user_group_data, resourceVersion=1)), content_type="application/json",
        headers=super_user_token)
    response_user = response.json.get("data")
    assert response.status_code == 200, response.json
    compare_dict_response(update_corp_user_group_data, response_user)
