# PayAPI — Learning x402 Through Building

A hands-on project to understand HTTP 402 payments and build payment-enabled APIs using Python.

## How x402 Works

1. **Request:** A client requests a resource from an API.
2. **Payment Required:** If payment is required, the server responds with HTTP `402 Payment Required` and provides the payment requirements.
3. **Payment:** The client creates the required payment payload and retries the request with the payment information.
4. **Verification:** The server or its configured payment facilitator verifies the payment according to the protocol.
5. **Resource Delivery:** If verification succeeds, the server provides the requested resource. Payment settlement is handled according to the configured payment flow.

## Project goals

- Understand the x402 payment protocol.
- Build an API with a free endpoint and a payment-protected endpoint.
- Learn how clients handle payment-required responses.
- Explore payment verification and settlement using the official SDK.
- Practice Git, testing, API documentation, and open-source development.

## Technology stack

- Python
- FastAPI
- x402 Python SDK
- Git and GitHub

## Learning progress

### Day 1 — Project setup

- [x] Set up the project directory.
- [x] Verify the installed Python and pip versions.
- [ ] Initialize Git and publish the repository.
- [ ] Understand the x402 protocol.
- [ ] Build the first API endpoint.

## What I learn

I'll document concepts, implementation decisions, errors, solutions, and useful references here as the project develops.

## Safety

Development and payment testing will use a supported test environment. No real funds or private keys should be committed to this repository.
