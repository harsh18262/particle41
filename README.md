# Particle41 Application

A minimalist time service application with Docker containerization and AWS cloud infrastructure deployment using Terraform.

## Repository

```bash
git clone https://github.com/harsh18262/particle41.git
```
## Architecture

This project demonstrates:
- Containerized application development with Docker
- Infrastructure as Code using Terraform
- AWS cloud deployment with ECS Fargate
- Content delivery via CloudFront

## Project Structure

```
particle41/
├── app/                    # Application source code and Docker files
├── terraform/              # Terraform infrastructure configuration
└── README.md              # This file
```

## Task 1 - Minimalist Application Development / Docker / Kubernetes

### Prerequisites

- Docker installed on your system
- Git for cloning the repository

### Steps to Build and Run the Application

1. **Clone the repository**
   ```bash
   git clone https://github.com/harsh18262/particle41.git
   ```

2. **Navigate to the application directory**
   ```bash
   cd app
   ```

3. **Build the Docker image**
   ```bash
   docker build -t simple-time-service .
   ```

4. **Run the Docker container**
   ```bash
   docker run -p 8080:8080 simple-time-service
   ```

5. **Access the application**
   
   Open your browser and navigate to:
   ```
   http://localhost:8080/
   ```

### Important Notes

- **Port Configuration**: The application uses port 8080 instead of privileged ports (like 80 or 443) because AWS ECS Fargate doesn't support running applications on privileged ports for security reasons.

- **macOS Compatibility**: On macOS, the application might not return a valid IP address as the container runs on a virtual machine rather than directly on the host system.

## Task 2 - Terraform and Cloud Infrastructure

### Prerequisites

- AWS CLI installed and configured
- Terraform installed on your system
- Valid AWS credentials with appropriate permissions

### Steps to Deploy Infrastructure

1. **Clone the repository** (if not already done)
   ```bash
   git clone https://github.com/harsh18262/particle41.git
   ```

2. **Navigate to the Terraform directory**
   ```bash
   cd terraform
   ```

3. **Setup AWS Credentials**
   ```bash
   aws configure
   ```
   
   You will be prompted to enter:
   - AWS Access Key ID
   - AWS Secret Access Key
   - Default region name
   - Default output format

4. **Initialize Terraform**
   ```bash
   terraform init
   ```

5. **Plan the infrastructure changes**
   ```bash
   terraform plan
   ```

6. **Apply the infrastructure changes**
   ```bash
   terraform apply
   ```

7. **Access the deployed application**
   
   Once the Terraform apply completes successfully, you can access the application using the CloudFront domain URL provided in the Terraform output.


## 🎯 Going Above and Beyond

This project includes additional automation and best practices to demonstrate a complete DevOps workflow - because why stop at just meeting requirements when you can gather some brownie points! 

## GitHub Actions CI/CD Pipeline

This project includes an automated GitHub Actions workflow for building and deploying the application.

### Workflow Overview

The pipeline consists of four jobs:
1. **Build**: Creates Docker image and pushes to Docker Hub
2. **Plan**: Generates Terraform execution plan
3. **Apply**: Deploys infrastructure to AWS (main branch only)
4. **Notify**: Reports deployment status

### Triggers

- **Push to main**: Full deployment pipeline
- **Push to develop**: Build and plan only  
- **Pull requests**: Build and plan with PR comments
- **Manual**: Via GitHub Actions UI

### Required GitHub Secrets

| Secret | Purpose |
|--------|---------|
| `DOCKERHUB_USERNAME` | Docker Hub authentication |
| `DOCKERHUB_TOKEN` | Docker Hub access token |
| `AWS_ACCESS_KEY_ID` | AWS access for Terraform |
| `AWS_SECRET_ACCESS_KEY` | AWS secret for Terraform |

### Setup Instructions

1. **Configure Docker Hub Token:**
   - Create access token in Docker Hub settings
   - Add as `DOCKERHUB_TOKEN` secret in GitHub

2. **Add AWS Credentials:**
   - Create IAM user with Terraform permissions
   - Add access keys as GitHub secrets

3. **Environment Protection (Optional):**
   - Go to Settings > Environments > Create `production`
   - Add manual approval requirements if desired

### Key Features

- **Automated deployment** on main branch pushes
- **Security scanning** with Trivy
- **Infrastructure planning** with Terraform
- **PR comments** showing planned changes
- **Production environment** protection

### Improvements
- It can have a remote backend for state management and locking.In this case it was not used to save costs.
- It can have caching enabled for docker images.
- It ca 

### Remote Backend Setup Using S3 and DynamoDB

For production deployments, it's recommended to use a remote Terraform backend with S3 and DynamoDB for state management and locking.


### Prerequisites

- AWS CLI installed and configured
- Terraform installed on your system
- Valid AWS credentials with appropriate permissions

#### Step 1: Create S3 Bucket and DynamoDB Table

First, create the required AWS resources for the remote backend:

```bash
# Create S3 bucket for Terraform state
aws s3 mb s3://your-terraform-state-bucket-name --region us-east-1

# Enable versioning on the S3 bucket this helps if the state is accidentally deleted or corrupted.
aws s3api put-bucket-versioning \
  --bucket your-terraform-state-bucket-name \
  --versioning-configuration Status=Enabled

# Create DynamoDB table for state locking
aws dynamodb create-table \
  --table-name terraform-state-locks \
  --attribute-definitions AttributeName=LockID,AttributeType=S \
  --key-schema AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region us-east-1
```

#### Step 2: Configure Terraform Backend

Add the following backend configuration to your `main.tf` or `terraform.tf` file in the terraform directory:

```hcl
terraform {
  backend "s3" {
    bucket         = "your-terraform-state-bucket-name"
    key            = "particle41/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-locks"
    encrypt        = true
  }
}
```

#### Step 3: Initialize with Remote Backend

```bash
# Navigate to terraform directory
cd terraform

# Initialize Terraform with the remote backend
terraform init

# If migrating from local state, Terraform will prompt to migrate
# Answer 'yes' when prompted to copy existing state to the new backend
```
Post this step, you can run `terraform plan` and `terraform apply` to deploy the infrastructure normally.