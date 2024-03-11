import boto3
import time
import argparse

def create_instance_from_encrypted_snapshot(encrypted_snapshot_id, dbclass):
    rds = boto3.client('rds')
    new_instance_id = f"restored-{encrypted_snapshot_id[:8]}"

    print(f"Starting creation of the new RDS instance {new_instance_id} from snapshot {encrypted_snapshot_id}...")

    # Create a new RDS instance from the encrypted snapshot
    rds.restore_db_instance_from_db_snapshot(
        DBInstanceIdentifier=new_instance_id,
        DBSnapshotIdentifier=encrypted_snapshot_id,
        DBInstanceClass=dbclass  # Use the provided instance class
        # Add other necessary parameters as needed
    )

    print(f"New RDS instance {new_instance_id} is being created from snapshot {encrypted_snapshot_id}.")

def cleanup_resources(old_instance_id):
    rds = boto3.client('rds')

    print(f"Starting deletion of the old RDS instance {old_instance_id}...")

    # Delete the old RDS instance
    rds.delete_db_instance(
        DBInstanceIdentifier=old_instance_id,
        SkipFinalSnapshot=True
    )

    print(f"Old RDS instance {old_instance_id} is being deleted.")

def main():
    parser = argparse.ArgumentParser(description='Script to create an RDS instance from an encrypted snapshot and clean up the old instance. Requires three arguments: encrypted_snapshot_id, dbclass, and old_instance_id.')
    parser.add_argument('encrypted_snapshot_id', type=str, help='Encrypted Snapshot ID')
    parser.add_argument('dbclass', type=str, help='DB Instance Class for the new RDS instance')
    parser.add_argument('old_instance_id', type=str, help='Old RDS Instance ID to delete')

    args = parser.parse_args()

    if not all([args.encrypted_snapshot_id, args.dbclass, args.old_instance_id]):
        parser.print_help()
        print("\nError: All three arguments are required: encrypted_snapshot_id, dbclass, and old_instance_id")
        exit(1)

    start_time = time.time()

    create_instance_from_encrypted_snapshot(args.encrypted_snapshot_id, args.dbclass)
    cleanup_resources(args.old_instance_id)

    total_time = time.time() - start_time
    print(f"\nTotal time for all processes: {total_time:.2f} seconds")

if __name__ == '__main__':
    main()
