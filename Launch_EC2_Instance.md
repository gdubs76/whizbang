# How to spin up an EC2 instance with AWS Management Console

To spin up (launch) an EC2 instance using the AWS Management Console, follow these steps:

## Step-by-Step Guide to Launch an EC2 Instance

**1. Sign in to the AWS Management Console**

- Go to the AWS Management Console and log in with your credentials.

**2. Select the Desired AWS Region**

- At the top right of the console, choose the AWS Region where you want to launch your instance. EC2 resources are region-specific.

**3. Navigate to the EC2 Console**

- In the search bar or under "Services," type and select **EC2** to open the EC2 Dashboard.

**4. Launch a New Instance**

- On the EC2 Dashboard, click the **Launch instance** button to start the launch wizard.

**5. Configure Your Instance**

- **Name and Tags:** Enter a descriptive name for your instance (optional but recommended).
- **Application and OS Images (AMI):** Choose the operating system for your instance (e.g., Amazon Linux, Ubuntu, Windows). For first-time users, Amazon Linux is recommended. Select an AMI marked "Free Tier eligible" if you want to use the free tier.
- **Instance Type:** Choose the instance type (e.g., t2.micro or t3.micro for Free Tier eligibility).
- **Key Pair (Login):** Select an existing key pair or create a new one for secure SSH access. Download and save the private key file if you create a new key pair—you’ll need it to connect to your instance.
- **Network Settings:** Configure network settings, such as allowing SSH (port 22) from your IP address for Linux or RDP (port 3389) for Windows.

**6. Review and Launch**

- Review your settings in the Summary panel.
- Click **Launch instance** to start the instance.

**7. Confirmation**

- You’ll see a success message confirming your instance is launching. The instance will appear in your EC2 Dashboard, where you can monitor its status.


## Quick Reference Table

| Step | Action |
| :-- | :-- |
| 1. Sign in | AWS Management Console |
| 2. Select Region | Choose region at top right |
| 3. Go to EC2 | Find EC2 in Services or search bar |
| 4. Launch Instance | Click "Launch instance" |
| 5. Configure | Name, AMI, Instance type, Key pair, Network settings |
| 6. Launch | Review and click "Launch instance" |
| 7. Confirm | Success message and view in EC2 Dashboard |

## Additional Tips

- **Charges:** You are billed for running instances, even if idle, unless using Free Tier eligible options.
- **Key Pair:** Keep your private key secure; you cannot download it again later.
- **Security:** Limit SSH/RDP access to trusted IPs only for better security.

This process will get your EC2 instance up and running via the AWS Management Console in just a few minutes.

[^1_12]: https://www.reddit.com/r/aws/comments/jzh7sb/spin_up_ec2_instances_run_commands_on_them_and/

[^1_13]: https://cloudmaven.github.io/cloud101_cloudproviders/01-aws-intro/

[^1_14]: https://aws.amazon.com/ec2/getting-started/

