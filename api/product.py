from api import router

@router.route("/product", methods=["GET"])
def product_get():
  return {
    "product": "product"
  }