# magfi.js
Mobile-API for [Magfi](https://magfi.co) app that helps you to find groups in the most popular messaging and social media apps

## Example
```JavaScript
async function main() {
	const { Magfi } = require("./magfi.js")
	const magfi = new Magfi()
	await magfi.login("email", "password")
}

main()
```
