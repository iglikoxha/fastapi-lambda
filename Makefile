all:
	docker compose up --build
test:
	curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{ \
		"resource": "/", \
		"path": "/", \
		"httpMethod": "GET", \
		"requestContext": { \
		  "resourcePath": "/", \
		  "httpMethod": "GET" \
		}, \
		"body": "{}" \
	}'