from skeleton.api import router
from skeleton.bootstrap import db

@router.route("/product", methods=["GET"])
def product_get():
  user = db.table('users').first()
  print(user)

  return {
    "product": "product",
    "user": user
  }
