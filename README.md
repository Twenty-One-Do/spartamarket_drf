## 🛒스파르타 마켓
- 스파르타 AI 6기 심화 과제
- 중고거래 사이트

## 📝프로젝트 소개
장고 및 DRF 실력 향상을 위한 CRUD 기능을 가진 중고거래 API 서버 개발

## 📅개발 기간
2024.04.30일 - 2024.05.01일 (2일)

## 🖥️개발 환경
- BE: Django, Django ORM, DRF, JWT

## 📜 ERD
![image](https://github.com/Twenty-One-Do/spartamarket_drf/assets/156996387/eb5947a2-770c-47a0-8541-4c6c3626d18f)

## 📜 API 명세

[Sparta Market.postman_collection.json](https://github.com/Twenty-One-Do/spartamarket_drf/files/15177076/Sparta.Market.postman_collection.json)

{
	"info": {
		"_postman_id": "d9478abd-8bf3-4168-a41d-3cdee2804771",
		"name": "Sparta Market",
		"description": "# 🚀 Get started here\n\nThis template guides you through CRUD operations (GET, POST, PUT, DELETE), variables, and tests.\n\n## 🔖 **How to use this template**\n\n#### **Step 1: Send requests**\n\nRESTful APIs allow you to perform CRUD operations using the POST, GET, PUT, and DELETE HTTP methods.\n\nThis collection contains each of these [request](https://learning.postman.com/docs/sending-requests/requests/) types. Open each request and click \"Send\" to see what happens.\n\n#### **Step 2: View responses**\n\nObserve the response tab for status code (200 OK), response time, and size.\n\n#### **Step 3: Send new Body data**\n\nUpdate or add new data in \"Body\" in the POST request. Typically, Body data is also used in PUT request.\n\n```\n{\n    \"name\": \"Add your name in the body\"\n}\n\n ```\n\n#### **Step 4: Update the variable**\n\nVariables enable you to store and reuse values in Postman. We have created a [variable](https://learning.postman.com/docs/sending-requests/variables/) called `base_url` with the sample request [https://postman-api-learner.glitch.me](https://postman-api-learner.glitch.me). Replace it with your API endpoint to customize this collection.\n\n#### **Step 5: Add tests in the \"Tests\" tab**\n\nTests help you confirm that your API is working as expected. You can write test scripts in JavaScript and view the output in the \"Test Results\" tab.\n\n<img src=\"https://content.pstmn.io/b5f280a7-4b09-48ec-857f-0a7ed99d7ef8/U2NyZWVuc2hvdCAyMDIzLTAzLTI3IGF0IDkuNDcuMjggUE0ucG5n\">\n\n## 💪 Pro tips\n\n- Use folders to group related requests and organize the collection.\n- Add more [scripts](https://learning.postman.com/docs/writing-scripts/intro-to-scripts/) in \"Tests\" to verify if the API works as expected and execute workflows.\n    \n\n## 💡Related templates\n\n[API testing basics](https://go.postman.co/redirect/workspace?type=personal&collectionTemplateId=e9a37a28-055b-49cd-8c7e-97494a21eb54&sourceTemplateId=ddb19591-3097-41cf-82af-c84273e56719)  \n[API documentation](https://go.postman.co/redirect/workspace?type=personal&collectionTemplateId=e9c28f47-1253-44af-a2f3-20dce4da1f18&sourceTemplateId=ddb19591-3097-41cf-82af-c84273e56719)  \n[Authorization methods](https://go.postman.co/redirect/workspace?type=personal&collectionTemplateId=31a9a6ed-4cdf-4ced-984c-d12c9aec1c27&sourceTemplateId=ddb19591-3097-41cf-82af-c84273e56719)",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "34440021"
	},
	"item": [
		{
			"name": "Product",
			"item": [
				{
					"name": "Products",
					"item": [
						{
							"name": "제품목록",
							"protocolProfileBehavior": {
								"disableBodyPruning": true
							},
							"request": {
								"method": "GET",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "order",
											"value": "latest",
											"type": "text"
										},
										{
											"key": "page",
											"value": "1",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/products/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"products",
										""
									]
								},
								"description": "- Authorization: X\n- Query String: X\n- body: O\n    \n\n## 소개\n\nproduct의 리스트를 보여주는 API입니다.\n\n페이지네이션, 정렬 기능이 있습니다.\n\n## 요청\n\nbody에 정렬을 위한 order 키와 페이지네이션을 위한 page 키가 있습니다.\n\n각각 미입력 시 \"latest\", \"1\"의 값으로 요청한 것과 같습니다.\n\norder에 올 수 있는 값은 latest, old, popular, views가 있습니다.\n\n각각 최신순, 오래된순, 인기순, 조회순을 의미합니다.\n\npage의 값이 정수형이 아니면 첫 페이지을 요청한 것과 같습니다.\n\npage의 값이 범위를 벗어나면 마지막 페이지를 요청한 것과 같습니다."
							},
							"response": []
						},
						{
							"name": "제품상세",
							"request": {
								"auth": {
									"type": "noauth"
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/api/products/1",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"products",
										"1"
									]
								},
								"description": "\n### GET /api/products/1\n\nThis endpoint retrieves the details of a specific product with the ID of 1.\n\n#### Request\n\nThis is a simple GET request with no request body.\n\n#### Response\n\nThe response will be a JSON object with the following schema:\n\n```json\n{\n  \"id\": \"number\",\n  \"title\": \"string\",\n  \"content\": \"string\",\n  \"writer\": \"number\",\n  \"likes_num\": \"number\",\n  \"views_num\": \"number\",\n  \"category\": \"number\",\n  \"image\": \"string | null\",\n  \"date_created\": \"string\",\n  \"last_updated\": \"string\",\n  \"comments\": [\n    {\n      \"id\": \"number\",\n      \"content\": \"string\",\n      \"date_created\": \"string\",\n      \"last_updated\": \"string\",\n      \"product\": \"number\",\n      \"writer\": \"number\"\n    }\n  ],\n  \"tags\": [\n    {\n      \"id\": \"number\",\n      \"name\": \"string\"\n    }\n  ]\n}\n```\n"
							},
							"response": []
						},
						{
							"name": "제품등록",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "JWT 토큰 입력",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "title",
											"value": "제목 입력 ",
											"type": "text"
										},
										{
											"key": "content",
											"value": "내용 입력 ",
											"type": "text"
										},
										{
											"key": "category",
											"value": "카테고리 아이디 입력 ",
											"type": "text"
										},
										{
											"key": "tags",
											"value": "해쉬태그 입력('#'로 구분, 한글만 입력)",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/products/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"products",
										""
									]
								},
								"description": "\n### POST /api/products/\n\nThis endpoint allows the client to create a new product by providing the title, content, category, and tags.\n\n#### Request Body\n- title (text, required): The title of the product.\n- content (text, required): The content or description of the product.\n- category (text, required): The category to which the product belongs.\n- tags (text, required): The tags associated with the product.\n\n#### Response\nThe response is in the JSON format and includes a status code of 400. The response body contains an array of validation errors related to the category field.\n\n#### Response JSON Schema\n```json\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"category\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  }\n}\n```\n"
							},
							"response": []
						},
						{
							"name": "제품수정",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "JWT 토큰 입력",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "content",
											"value": "수정할 내용 입력",
											"type": "text"
										},
										{
											"key": "category",
											"value": "수정할 카테고리 아이디 입력",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/products/1",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"products",
										"1"
									]
								},
								"description": "### Update Product Details\n\nThis endpoint allows updating the details of a specific product.\n\n#### Request Body\n\n- form-data\n    - content (text, optional): Description of the product.\n    - category (text, optional): Category of the product.\n\n#### Response\n\nThe response is in JSON format and has the following schema:\n\n``` json\n{\n    \"type\": \"object\",\n    \"properties\": {\n        \"id\": {\n            \"type\": \"integer\"\n        },\n        \"title\": {\n            \"type\": \"string\"\n        },\n        \"content\": {\n            \"type\": \"string\"\n        },\n        \"writer\": {\n            \"type\": \"integer\"\n        },\n        \"likes_num\": {\n            \"type\": \"integer\"\n        },\n        \"views_num\": {\n            \"type\": \"integer\"\n        },\n        \"category\": {\n            \"type\": \"integer\"\n        },\n        \"image\": {\n            \"type\": [\"string\", \"null\"]\n        },\n        \"date_created\": {\n            \"type\": \"string\"\n        },\n        \"last_updated\": {\n            \"type\": \"string\"\n        }\n    }\n}\n\n ```"
							},
							"response": []
						},
						{
							"name": "제품삭제",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "JWT 토큰 입력 ",
											"type": "string"
										}
									]
								},
								"method": "DELETE",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/api/products/3",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"products",
										"3"
									]
								},
								"description": "### Delete Product\n\nThis endpoint is used to delete a specific product.\n\n#### Request\n\n- Method: DELETE\n- URL: `http://127.0.0.1:8000/api/products/3`\n    \n\n#### Response\n\nThe response is in JSON format with the following schema:\n\n``` json\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"detail\": {\n      \"type\": \"string\"\n    }\n  }\n}\n\n ```\n\n- Status: 404\n- Content-Type: application/json\n- Body:\n    \n    ``` json\n    {\n      \"detail\": \"string\"\n    }\n    \n     ```"
							},
							"response": []
						}
					]
				},
				{
					"name": "Comments",
					"item": [
						{
							"name": "댓글목록",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/api/products/8/comments/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"products",
										"8",
										"comments",
										""
									]
								}
							},
							"response": []
						},
						{
							"name": "댓글등록",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "JWT 토큰 입력",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "content",
											"value": "댓글 내용 입력",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/products/1/comments/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"products",
										"1",
										"comments",
										""
									]
								}
							},
							"response": []
						},
						{
							"name": "댓글수정",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "JWT 토큰 입력 ",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "content",
											"value": "댓글 내용 입력",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/products/comments/5",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"products",
										"comments",
										"5"
									]
								}
							},
							"response": []
						},
						{
							"name": "댓글삭제",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "JWT 토큰 입력",
											"type": "string"
										}
									]
								},
								"method": "DELETE",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/api/products/comments/5",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"products",
										"comments",
										"5"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "Likes",
					"item": [
						{
							"name": "좋아요",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "JWT 토큰 입력",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "what",
											"value": "포스트 번호 입력 ",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/products/likes/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"products",
										"likes",
										""
									]
								}
							},
							"response": []
						}
					]
				}
			]
		},
		{
			"name": "Account",
			"item": [
				{
					"name": "Auth",
					"item": [
						{
							"name": "로그인",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "username",
											"value": "아이디 입력",
											"type": "text"
										},
										{
											"key": "password",
											"value": "비밀번호 입력",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/accounts/login/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"accounts",
										"login",
										""
									]
								}
							},
							"response": []
						},
						{
							"name": "갱신 토큰 블랙리스트",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "refresh",
											"value": "갱신 토큰 입력",
											"type": "text"
										},
										{
											"key": "access",
											"value": "액세스 토큰 입력",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/accounts/refresh/blacklist",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"accounts",
										"refresh",
										"blacklist"
									]
								}
							},
							"response": []
						},
						{
							"name": "갱신",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "refresh",
											"value": "갱신 토큰 입력",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/accounts/refresh/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"accounts",
										"refresh",
										""
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "AccountsCRUD",
					"item": [
						{
							"name": "회원가입",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "name",
											"value": "이름 입력",
											"type": "text"
										},
										{
											"key": "age\n",
											"value": "나이 입력",
											"type": "text"
										},
										{
											"key": "email",
											"value": "이메일 입력",
											"type": "text"
										},
										{
											"key": "nickname",
											"value": "닉네임 입력",
											"type": "text"
										},
										{
											"key": "username",
											"value": "아이디 입력",
											"type": "text"
										},
										{
											"key": "password",
											"value": "비밀번호",
											"type": "text"
										},
										{
											"key": "password2",
											"value": "비밀번호 확인",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/accounts/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"accounts",
										""
									]
								}
							},
							"response": []
						},
						{
							"name": "회원정보",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "JWT 토큰 입력",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "http://127.0.0.1:8000/api/accounts/5",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"accounts",
										"5"
									]
								}
							},
							"response": []
						},
						{
							"name": "회원수정",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "JWT 토큰 입력",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "name",
											"value": "이름 ",
											"type": "text"
										},
										{
											"key": "age\n",
											"value": "나이",
											"type": "text"
										},
										{
											"key": "email",
											"value": "이메일",
											"type": "text"
										},
										{
											"key": "nickname",
											"value": "닉네임",
											"type": "text"
										},
										{
											"key": "username",
											"value": "아이디",
											"type": "text"
										},
										{
											"key": "password",
											"value": "비밀번호",
											"type": "text"
										},
										{
											"key": "password2",
											"value": "비밀번호 확인",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/accounts/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"accounts",
										""
									]
								}
							},
							"response": []
						},
						{
							"name": "비밀번호수정",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "JWT 토큰 입력",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "original_password",
											"value": "기존 비밀번호",
											"type": "text"
										},
										{
											"key": "new_password",
											"value": "새로운 비밀번호",
											"type": "text"
										},
										{
											"key": "new_password2",
											"value": "새로운 비밀번호 확인",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/accounts/password/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"accounts",
										"password",
										""
									]
								}
							},
							"response": []
						},
						{
							"name": "회원탈퇴",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "JWT 토큰 입력",
											"type": "string"
										}
									]
								},
								"method": "DELETE",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "password",
											"value": "기존 비밀번호",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/accounts/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"accounts",
										""
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "Follow",
					"item": [
						{
							"name": "follow",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "JWT 토큰 입력",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "formdata",
									"formdata": [
										{
											"key": "whom",
											"value": "팔로우할 회원의 pk\n",
											"type": "text"
										}
									]
								},
								"url": {
									"raw": "http://127.0.0.1:8000/api/accounts/follow/",
									"protocol": "http",
									"host": [
										"127",
										"0",
										"0",
										"1"
									],
									"port": "8000",
									"path": [
										"api",
										"accounts",
										"follow",
										""
									]
								}
							},
							"response": []
						}
					]
				}
			]
		}
	],
	"event": [
		{
			"listen": "prerequest",
			"script": {
				"type": "text/javascript",
				"exec": [
					""
				]
			}
		},
		{
			"listen": "test",
			"script": {
				"type": "text/javascript",
				"exec": [
					""
				]
			}
		}
	],
	"variable": [
		{
			"key": "id",
			"value": "1"
		},
		{
			"key": "base_url",
			"value": "https://postman-rest-api-learner.glitch.me/"
		}
	]
}
