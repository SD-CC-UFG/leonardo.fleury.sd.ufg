import datetime
import json
import re
import logging

from nameko.rpc import rpc
from bson.objectid import ObjectId
from bson.json_util import dumps
from bcrypt import hashpw, gensalt

from users.database import get_db

log = logging.getLogger(__name__)

class Users(object):
    name = "users"

    @rpc
    def create_user(self, username, password):
        mongo = get_db()
        # TODO: Password should have at least 6 characters
        if not self.__username_is_valid(username):
            return 1

        user = {
            '_id': username,
            'password': hashpw(password.encode('utf-8'), gensalt()),
            'created': datetime.datetime.utcnow()
        }

        user_id = mongo.insert_one(user).inserted_id

        log.info("New user created.")
        log.debug("New user: {} created.".format(user_id))

        return json.dumps({
            "code": 0,
            "user_id": user_id
        })

    @rpc
    def update_user_password(self, username, old_password, new_password):
        mongo = get_db()

        old_hash = mongo.find_one({'_id': username})['password']

        if (hashpw(old_password.encode('utf-8'), old_hash) == old_hash):
            new_hash = hashpw(new_password.encode('utf-8'), gensalt())

            user = {'$set': {'password': new_hash}}

            mod_count = mongo.update_one(
                {'_id': username}, user).modified_count

            if mod_count is not 0:
                log.info("{} changed password".format(username))
                return json.dumps({
                    "code": 0,
                    "modified_count": mod_count
                })
            else:
                log.error("Could not change password from user {}.".format(username))
                return json.loads({
                    "code": 1,
                    "error": "Could not change password from user {}.".format(username)
                })

            log.error("Something happened...")
            return json.loads({
                    "code": 3,
                    "error": "Something happened..."
                })
        else:
            log.error("Incorrect password.")
            return json.loads({
                    "code": 2,
                    "error": "Incorrect password."
                })

    @rpc
    def delete_user(self, username):
        mongo = get_db()
        deleted = mongo.delete_one({"_id": username}).deleted_count

        if deleted:
            log.info("User {} deleted.".format(username))
            return json.dumps({
                    "code": 0,
                    "deleted_count": deleted
                })
        else:
            log.error("User {} could not be deleted.".format(username))
            return json.dumps({
                    "code": 1,
                    "error": "User {} could not be deleted.".format(username)
                })

    @rpc
    def view_user(self, username):
        mongo = get_db()

        user = mongo.find_one({"_id": username})

        return json.dumps({
                    "code": 0,
                    "user": {
                        "user_id": user["_id"],
                        # "created_at": user["created"]
                    }
                })

    def __username_is_valid(self, username):
        # TODO: Test username for null character

        if (username is "") or ('$' in username) or (username.startswith('system.')):
            return False

        return True

    def __password_is_valid(self, password):
        pass
