import requests

class Magfi:
	def __init__(
			self,
			country_code: str = "ru") -> None:
		self.api = "http://api.magfiads.com/app"
		self.identity_toolkit_api = "https://www.googleapis.com/identitytoolkit/v3/relyingparty"
		self.headers = {
			"user-agent": "Dart/2.13 (dart:io)"
		}
		self.user_id = None
		self.id_token = None
		self.country_code = country_code
		self.api_key = "AIzaSyAEf31Du8kcON5uudUfSRHNZ6u8Ydg6wZ0"

	def login(
			self,
			email: str,
			password: str) -> dict:
		data = {
			"email": email,
			"password": password,
			"returnSecureToken": True
		}
		response = requests.post(
			f"{self.identity_toolkit_api}/verifyPassword?key={self.api_key}",
			data=data,
			headers=self.headers).json()
		if "idToken" in response:
			self.user_id = response["localId"]
			self.id_token = response["idToken"]
		return response

	def register(
			self,
			email: str,
			password: str) -> dict:
		data = {
			"email": email,
			"password": password
		}
		return requests.post(
			f"{self.identity_toolkit_api}/signupNewUser?key={self.api_key}",
			data=data,
			headers=self.headers).json()

	def get_account_info(self) -> dict:
		data = {
			"idToken": self.id_token
		}
		return requests.post(
			f"{self.api}/getAccountInfo?key={self.api_key}",
			data=data,
			headers=self.headers).json()

	def get_app_version(self) -> dict:
		return requests.get(
			f"{self.api}/app-version",
			headers=self.headers).json()

	def get_main_page(self) -> dict:
		return requests.get(
			f"{self.api}app/main-page?userID={self.user_id}",
			headers=self.headers).json()

	def get_cat_names(self) -> list:
		return requests.get(
			f"{self.api}/app-cat-names",
			headers=self.headers).json()

	def get_user_follow_count(
			self,
			user_id: str) -> dict:
		return requests.get(
			f"{self.api}/follow-count?userID={user_id}",
			headers=self.headers).json()

	def get_user_followers(
			self,
			user_id: str) -> list:
		return requests.get(
			f"{self.api}/followers?userID={user_id}",
			headers=self.headers).json()

	def get_user_followings(
			self,
			user_id: str) -> list:
		return requests.get(
			f"{self.api}/following?userID={user_id}",
			headers=self.headers).json()

	def get_categories(self) -> list:
		return requests.get(
			f"{self.api}/category-list?country_code={self.country_code}",
			headers=self.headers).json()

	def get_suggested_users(self) -> list:
		return requests.get(
			f"{self.api}/suggested-users?userID={self.user_id}",
			headers=self.headers).json()

	def get_feed(self, page: int = 1) -> list:
		return requests.get(
			f"{self.api}/FeedInfinty?page={page}&userID={self.user_id}",
			headers=self.headers).json()

	def get_trends(self) -> list:
		return requests.get(
			f"{self.api}/app/trends",
			headers=self.headers).json()

	def get_language_region(self) -> list:
		return requests.get(
			f"{Self.api}/language-region?country_code={self.country_code}",
			headers=self.headers).json()

	def change_password(
			self,
			password: str) -> dict:
		data = {
			"returnSecureToken": True,
			"idToken": self.id_token,
			"password": password
		}
		return requests.post(
			f"{self.identity_toolkit_api}/setAccountInfo?key={self.api_key}",
			data=data,
			headers=self.headers).json()
