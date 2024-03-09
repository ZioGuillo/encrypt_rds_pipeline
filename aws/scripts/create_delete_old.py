import boto3
import time

def create_instance_from_encrypted_snapshot(encrypted_snapshot_id):
    rds = boto3.client('rds')
    new_instance_id = f"restored-{encrypted_snapshot_id[:8]}"

    print(f"Starting creation of the new RDS instance {new_instance_id} from snapshot {encrypted_snapshot_id}...")
    start_time = time.time()

    # Create a new RDS instance from the encrypted snapshot
    rds.restore_db_instance_from_db_snapshot(
        DBInstanceIdentifier=new_instance_id,
        DBSnapshotIdentifier=encrypted_snapshot_id,
        DBInstanceClass='db.m4.large'  # Example instance class
        # Add other necessary parameters as needed
    )

    end_time = time.time()
    print(f"New RDS instance {new_instance_id} is being created from snapshot {encrypted_snapshot_id}.")
    return end_time - start_time

def cleanup_resources(old_instance_id):
    rds = boto3.client('rds')

    print(f"Starting deletion of the old RDS instance {old_instance_id}...")
    start_time = time.time()

    # Delete the old RDS instance
    rds.delete_db_instance(
        DBInstanceIdentifier=old_instance_id,
        SkipFinalSnapshot=True
    )

    end_time = time.time()
    print(f"Old RDS instance {old_instance_id} is being deleted.")
    return end_time - start_time

def main():
    encrypted_snapshot_id = input("Enter the Encrypted Snapshot ID: ")
    old_instance_id = input("Enter the Old RDS Instance ID to delete: ")

    creation_time = create_instance_from_encrypted_snapshot(encrypted_snapshot_id)
    cleanup_time = cleanup_resources(old_instance_id)

    print(f"\nTime to create new instance from snapshot: {creation_time:.2f} seconds")
    print(f"Time to cleanup old resources: {cleanup_time:.2f} seconds")

if __name__ == '__main__':
    main()
