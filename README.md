# Kapture Finance Collections Agent

An AI-powered voice collections agent built using Vapi for the Kapture Finance Task 2 assignment.

## Project Overview

This project implements an outbound voice agent for respectful follow-up on overdue loan EMIs.

The agent is designed to:

- Verify the customer's identity before revealing sensitive account information.
- Explain the overdue EMI after successful verification.
- Understand the customer's payment intent.
- Capture a promise-to-pay when the customer provides a clear payment date and amount.
- Handle edge cases such as already-paid claims and financial hardship.
- Avoid making unsupported claims or financial/legal advice.
- End calls politely when the conversation is complete.

## Technology

- Vapi
- OpenAI language model
- Voice-based conversational AI
- Vapi Tools / Functions
- Webhook-based integrations
- GitHub

## Conversation Flow

1. Introduce Kapture Finance and request identity verification.
2. Verify the customer.
3. Do not reveal debt information before verification.
4. Explain the overdue EMI after verification.
5. Ask about payment intent.
6. If the customer can pay, collect:
   - Payment amount
   - Payment date
7. Log the promise-to-pay.
8. Recap the commitment.
9. End the call politely.

## Guardrails

The agent must:

- Never reveal overdue amounts or loan information before verification.
- Never disclose information to a wrong person.
- Never pressure, threaten, shame, or make legal claims.
- Never provide financial, legal, or credit advice.
- Never claim that a payment was made unless a configured system confirms it.
- Never claim that an account was updated unless the appropriate tool confirms it.
- Never claim that a payment link was sent unless the configured tool confirms it.
- Direct customers to official channels for unresolved matters.
- Handle hardship and disputes empathetically.

## Tools

The agent uses tools/functions for operational actions such as:

- verify_customer
- log_promise_to_pay
- end_collections_call

These tools allow the conversation flow to be controlled and prevent the assistant from claiming that an action occurred when it was not actually executed.

## Tested Scenarios

### 1. Successful Promise-to-Pay

The customer verifies their identity and agrees to pay:

- Amount: ₹5,000
- Date: 28 August 2026

The Log Promise To Pay tool completed successfully.

### 2. Financial Hardship

The customer states that they cannot make the payment because of financial hardship.

The agent:

- Acknowledges the situation empathetically.
- Does not promise an accommodation.
- Explains that a specialist may need to review the situation.
- Directs the customer to the official channel.

### 3. Already Paid

The customer states that the EMI has already been paid.

The agent:

- Acknowledges the claim.
- Does not claim that the payment is confirmed.
- Explains that the account may need specialist review.
- Directs the customer to the official customer-service channel.

## Testing

The agent was tested using multiple conversation paths, including:

- Successful identity verification
- Successful promise-to-pay
- Missing/unclear payment date
- Financial hardship
- Already-paid claim
- Conversation closing
- Tool execution and completion

## Demo

A working Vapi voice-agent demo was created and tested using Vapi's Talk interface.

Demo evidence and call recordings/screenshots are included with the project submission.

## Architecture

The system follows this high-level flow:

Customer
   |
   v
Vapi Voice Agent
   |
   v
Identity Verification
   |
   +---- Verification Failed ---> End Call
   |
   v
Overdue EMI Discussion
   |
   +---- Already Paid -------> Specialist / Official Channel
   |
   +---- Financial Hardship -> Specialist / Official Channel
   |
   +---- Can Pay ------------> Promise-to-Pay
                                      |
                                      v
                              Log Commitment
                                      |
                                      v
                                  End Call

## Future Improvements

With additional development time, the system could be extended with:

- Real payment-link generation
- SMS/WhatsApp payment-link delivery
- CRM integration
- Automated payment-status verification
- Hindi/English bilingual conversations
- Automated evaluation of call quality
- Larger-scale test/evaluation framework
- Production monitoring and analytics

## Submission

This repository contains the project documentation and implementation artifacts for the Kapture Finance AI voice collections agent.

Sensitive credentials and private account information are intentionally excluded.