from skeleton.api import router

@router.route("/user", methods=["GET"])
def user_get():
  return {
    "user": "user"
  }
