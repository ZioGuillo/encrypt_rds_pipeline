import boto3

def create_instance_from_encrypted_snapshot(encrypted_snapshot_id):
    rds = boto3.client('rds')
    new_instance_id = f"restored-{encrypted_snapshot_id[:8]}"

    # Create a new RDS instance from the encrypted snapshot
    rds.restore_db_instance_from_db_snapshot(
        DBInstanceIdentifier=new_instance_id,
        DBSnapshotIdentifier=encrypted_snapshot_id,
        DBInstanceClass='db.m4.large'  # Example instance class
        # Add other necessary parameters as needed
    )
    print(f"New RDS instance {new_instance_id} is being created from snapshot {encrypted_snapshot_id}.")

def cleanup_resources(old_instance_id):
    rds = boto3.client('rds')

    # Delete the old RDS instance
    rds.delete_db_instance(
        DBInstanceIdentifier=old_instance_id,
        SkipFinalSnapshot=True
    )
    print(f"Old RDS instance {old_instance_id} is being deleted.")

def main():
    encrypted_snapshot_id = input("Enter the Encrypted Snapshot ID: ")
    old_instance_id = input("Enter the Old RDS Instance ID to delete: ")

    create_instance_from_encrypted_snapshot(encrypted_snapshot_id)
    cleanup_resources(old_instance_id)

if __name__ == '__main__':
    main()
