📁 Google Drive Clone Using AWS (Serverless Project)
📌 Project Overview

This project is a Google Drive Clone UI where users can view files that are stored in Amazon S3 Cloud Storage.

The frontend is built using HTML, CSS, and JavaScript, and the backend is built using AWS Serverless services such as API Gateway, Lambda, and S3.

The main goal of this project is to understand how a frontend application can communicate with AWS cloud services to fetch and display data in real time.

🖥 Application Preview (UI)

This is the frontend Google Drive Clone interface showing files loaded from AWS S3.

<img width="1919" height="867" alt="Screenshot 2026-02-05 002311" src="https://github.com/user-attachments/assets/b82b2e6d-3a13-490e-bb08-2b53d133f30c" />


🏗 Architecture Diagram

Below is the architecture used in this project:

User
   ↓
Google Drive Clone UI (HTML, CSS, JavaScript)
   ↓
API Gateway
   ↓
Lambda Function
   ↓
Amazon S3 Bucket (Cloud Storage)

<img width="1536" height="1024" alt="ChatGPT Image Feb 4, 2026, 11_48_59 PM" src="https://github.com/user-attachments/assets/d70b57e7-6135-461d-bf37-b1208fe701fa" />


☁ Amazon S3 Bucket Preview

This shows the files stored inside the S3 bucket which are displayed in the UI.

<img width="1557" height="621" alt="Screenshot 2026-02-05 002410" src="https://github.com/user-attachments/assets/08ae4ebf-71d6-488d-84ba-0c240c72d4d4" />


🌐 API Gateway Preview

This shows the API Gateway configuration and deployed endpoints connected to Lambda.

<img width="1556" height="622" alt="Screenshot 2026-02-05 002528" src="https://github.com/user-attachments/assets/964c3ec4-3ea4-4ee0-b70f-c69f77800570" />


⚙ Technologies Used
Frontend:

HTML

CSS

JavaScript

AWS Cloud Services:

Amazon S3 (Storage)

AWS Lambda (Backend Logic)

API Gateway (API Connection)

IAM Role (Permissions)

🚀 How This Project Works
Step 1 — Create S3 Bucket (Cloud Storage)

I created an Amazon S3 bucket.

Uploaded some sample files (PDF, images, documents).

These files act as the cloud storage data.

S3 is used as:

Secure cloud storage

Highly scalable

Fast file access system

Step 2 — Create IAM Role

I created an IAM Role for Lambda.

Attached permission:

AmazonS3FullAccess


This allows the Lambda function to:

Read files from S3

List bucket objects

Generate download links

Step 3 — Create Lambda Function

I created a Lambda function using Python.

Inside Lambda, I added logic to:

✅ Fetch file list from S3
✅ Generate secure download URLs
✅ Return data to API Gateway

Lambda acts as the backend server without managing any physical servers.

Step 4 — Create API Gateway

Created REST API in API Gateway.

Created resources and methods.

Connected API Gateway with Lambda function.

Enabled CORS for browser access.

Deployed the API to a production stage.

After deployment, API Gateway provided an Invoke URL.

Step 5 — API Testing

To verify everything is working:

I pasted the API URL directly into the browser.

If the S3 files list appears → connection is successful ✅

If not → configuration issue ❌

This step helped confirm:

Lambda is connected to S3

API Gateway is working properly

Step 6 — Frontend Integration

I added the API Gateway URL inside JavaScript code.

The frontend fetches file data using the API.

The UI dynamically displays files stored in S3.

Now when users open the UI:

✅ Files are loaded from cloud
✅ Real-time data is displayed
✅ Cloud storage is connected

📂 Project Features

✔ Google Drive style UI
✔ Real-time S3 file listing
✔ Serverless backend
✔ Secure cloud storage
✔ No server management
✔ Fully cloud-integrated architecture
