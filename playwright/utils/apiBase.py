from playwright.sync_api import Playwright

ordersPlayload = {"orders": [{
    "country": "India",
    "productOrderedId": "6960eae1c941646b7a8b3ed3"
}]}

class APIUtils:
    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login", data={"userEmail":"lotela9945@ellbit.com", "userPassword":"#Punisher01"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order", data=ordersPlayload, headers={"authorization": token, "Content-Type": "application/json"})
        print(response.json())
        response_body = response.json()
        orderID = response_body["orders"][0]
        return orderID