# Particle41 Application

A minimalist time service application with Docker containerization and AWS cloud infrastructure deployment using Terraform.

## Repository

```bash
git clone https://github.com/harsh18262/particle41.git
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

## Support

For issues or questions, please refer to the repository's issue tracker or documentation.
 