import boto3

def list_rds_instances():
    rds = boto3.client('rds')
    instances = rds.describe_db_instances()
    if not instances['DBInstances']:
        print("No RDS instances found in the account.")
        exit()
    return {db['DBInstanceIdentifier']: db for db in instances['DBInstances']}

def create_and_encrypt_snapshot(instance_id, kms_key_id):
    rds = boto3.client('rds')
    snapshot_id = f"{instance_id}-snapshot"
    encrypted_snapshot_id = f"{snapshot_id}-encrypted"

    # Create a snapshot
    rds.create_db_snapshot(
        DBSnapshotIdentifier=snapshot_id,
        DBInstanceIdentifier=instance_id
    )
    print(f"Snapshot {snapshot_id} created.")

    # Encrypt the snapshot
    rds.copy_db_snapshot(
        SourceDBSnapshotIdentifier=snapshot_id,
        TargetDBSnapshotIdentifier=encrypted_snapshot_id,
        KmsKeyId=kms_key_id,
        CopyTags=True
    )
    print(f"Encrypted snapshot {encrypted_snapshot_id} created.")

    return snapshot_id, encrypted_snapshot_id, instance_id

def main():
    instances = list_rds_instances()
    if instances:
        for id, details in instances.items():
            kms_key_id = details.get('KmsKeyId', 'No KMS Key')
            print(f"{id}: Status = {details.get('DBInstanceStatus')}, KMS Key ID = {kms_key_id}")

        selected_instance = input("Enter the RDS instance ID to snapshot and encrypt: ")
        selected_kms_key = input("Enter the KMS Key ID to use for encryption (leave blank to use default): ")
        if not selected_kms_key:
            selected_kms_key = 'alias/aws/rds'  # default KMS key for RDS

        snapshot_id, encrypted_snapshot_id, instance_id = create_and_encrypt_snapshot(selected_instance, selected_kms_key)

        print(f"\nSnapshot ID: {snapshot_id}")
        print(f"Encrypted Snapshot ID: {encrypted_snapshot_id}")
        print(f"Original RDS Instance ID: {instance_id}")

if __name__ == '__main__':
    main()
