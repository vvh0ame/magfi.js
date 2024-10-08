class Magfi {
	constructor(countryCode = "ru") {
		this.api = "http://api.magfiads.com/app"
		this.identityToolkitApi = "https://www.googleapis.com/identitytoolkit/v3/relyingparty"
		this.headers = {
			"user-agent": "Dart/2.13 (dart:io)"
		}
		this.countryCode = countryCode
		this.apiKey = "AIzaSyAEf31Du8kcON5uudUfSRHNZ6u8Ydg6wZ0"
	}


	async login(email, password) {
		const response = await fetch(
			`${this.identityToolkitApi}/verifyPassword?key=${this.apiKey}`, {
				method: "POST",
				body: JSON.stringify({
					email: email,
					password: password,
					returnSecureToken: true
				}),
				headers: this.headers
			})
		const data = await response.json()
		if ("idToken" in data) {
			this.userId = data.localId
			this.idToken = data.idToken
		}
		return data
	}

	async register(email, password) {
		const response = await fetch(
			`${this.identityToolkitApi}/signupNewUser?key=${this.apiKey}`, {
				method: "POST",
				body: JSON.stringify({
					email: email,
					password: password
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getAccountInfo() {
		const response = await fetch(
			`${this.api}/getAccountInfo?key=${this.apiKey}`, {
				method: "POST",
				body: JSON.stringify({
					idToken: this.idToken
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getAppVersion() {
		const response = await fetch(
			`${this.api}/app-version`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getMainPage() {
		const response = await fetch(
			`${this.api}/app/main-page?userID=${this.userId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCatNames() {
		const response = await fetch(
			`${this.api}/app-cat-names`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async  getUserFollowers(userId) {
		const response = await fetch(
			`${this.api}/followers?userID=${userId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async  getUserFollowings(userId) {
		const response = await fetch(
			`${this.api}/following?userID=${userId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getSuggestedUsers() {
		const response = await fetch(
			`${this.api}/suggested-users?userID=${this.userId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getFeed(page = 1) {
		const response = await fetch(
			`${this.api}/FeedInfinty?page=${page}&userID=${this.userId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getTrends() {
		const response = await fetch(
			`${this.api}/app/trends`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}
}

module.exports = {Magfi}
