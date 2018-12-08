import datetime
import json
import re
import logging

from nameko.rpc import rpc
from bson.objectid import ObjectId
from bson.json_util import dumps
from bcrypt import hashpw, gensalt

from users.database import get_db

log = logger = logging.getLogger(__name__)

class Users(object):
    name = "users"

    @rpc
    def create_user(self, username, password):
        mongo = get_db()
        # TODO: Test username for empty string, `$` character, null character or begin with `system.`
        # TODO: Password should have at least 6 characters
        user = {
            '_id': username,
            'password': hashpw(password.encode('utf-8'), gensalt()),
            'created': datetime.datetime.utcnow()
        }

        user_id = mongo.insert_one(user).inserted_id

        log.info("New user created.")
        log.debug("New user: {} created.".format(user_id))

        return dumps(user_id)

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
                return json.dumps({'code': 0, 'success': 'Password modified'})
            else:
                log.info("Could not change password from user {}.".format(username))
                return json.dumps({'code': 1, 'error': 'Password could not be modified. Try again.'})

            log.info("Something happened...")
            return dumps(mod_count)
        else:
            log.info("Incorrect password.")
            return json.dumps({'code': 2, 'error': 'Incorrect password.'})

    @rpc
    def delete_user(self, username):
        mongo = get_db()
        deleted = mongo.delete_one({"_id": username}).deleted_count

        if deleted:
            log.info("User {} deleted.".format(username))
            return json.dumps({'code': 0, 'success': "User deleted with success."})
        else:
            log.info("User {} could not be deleted.".format(username))
            return json.dumps({'code': 1, 'error': "Could not delete user. Try again."})

    @rpc
    def view_user(self, username):
        mongo = get_db()

        user = mongo.find_one({"_id": username})

        return dumps(user)

    def __validate_username(self, username):
        pass

    def __validate_password(self, password):
        pass
