# High-Level Design (HLD)

## 1. System Overview

The Kapture Finance Collections Agent is an AI-powered outbound voice agent built using Vapi.

Its purpose is to conduct respectful follow-up calls with customers regarding overdue loan EMIs while enforcing identity verification and conversation guardrails.

## 2. Architecture

```text
Customer
   |
   v
Vapi Voice Agent
   |
   v
Identity Verification
   |
   +---- Verification Failed ----> End Call
   |
   v
Overdue EMI Discussion
   |
   +---- Already Paid --------> Official Channel / Specialist
   |
   +---- Financial Hardship --> Specialist / Official Channel
   |
   +---- Can Pay -------------> Promise-to-Pay
                                      |
                                      v
                              Log Promise To Pay
                                      |
                                      v
                                  End Call