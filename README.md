
# Encrypt RDS Pipeline

## Overview

The `encrypt_rds_pipeline` project provides a set of Python scripts designed to automate the encryption process of Amazon RDS instances, prioritizing data security and compliance with CMMC and SOC2 requirements. This project helps organizations enhance their security posture by automating the creation of encrypted snapshots of existing RDS instances and launching new RDS instances from these encrypted snapshots, followed by cleaning up old, unencrypted instances and snapshots.

## Prerequisites

- Python 3.x
- AWS CLI installed and configured with necessary permissions
- Boto3 library installed (`pip install boto3`)

## Configuration

Ensure your AWS CLI is configured with the correct credentials and default region by running:

```bash
aws configure
```

## Usage

### Step 1: Create and Encrypt Snapshot

Run the `create_and_encrypt_snapshot.py` script to create an encrypted snapshot of an existing RDS instance. This step is crucial for meeting the stringent security requirements of CMMC and SOC2 by ensuring data at rest is encrypted.

```bash
python create_and_encrypt_snapshot.py
```

### Step 2: Create RDS Instance from Encrypted Snapshot and Cleanup

After the encrypted snapshot is created, run the `create_instance_and_cleanup.py` script to create a new RDS instance from the encrypted snapshot and clean up the old resources. This step reinforces the commitment to data security and regulatory compliance.

```bash
python create_instance_and_cleanup.py
```

## Scripts

- `create_and_encrypt_snapshot.py`: Lists RDS instances, creates a snapshot of the selected instance, and then creates an encrypted copy of the snapshot, adhering to security and compliance standards.
- `create_instance_and_cleanup.py`: Input the last Snapshot Encrypted, creates a new RDS instance from this snapshot, and cleans up the old RDS instance and snapshot, maintaining the integrity and security of the data.

## Security and Compliance

This project emphasizes the importance of data security and compliance with standards like CMMC and SOC2. By automating the encryption of RDS instances, it ensures that sensitive data is protected, thereby supporting organizations in meeting their security and regulatory obligations.

## Contributing

Feel free to fork the repository and submit pull requests to contribute to the project.

## License

Specify your license here or indicate if the project is open source.
