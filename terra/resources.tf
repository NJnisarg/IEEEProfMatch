resource "aws_elastic_beanstalk_application" "IEEEProfMatch" {
  name = "IEEEProfMatch"
  description = "IEEE Prof Match project"
}

resource "aws_elastic_beanstalk_environment" "IEEEProfMatch-test" {
  name = "IEEEProfMatch-test"
  description = "Test Environment for IEEE ProfMatch project"
  application = "${aws_elastic_beanstalk_application.IEEEProfMatch.name}"
}

resource "aws_s3_bucket" "app_versioning_bucket" {
  bucket = "elasticbeanstalk-us-east-1-369554917544"
}

resource "aws_s3_bucket_policy" "app_versioning_bucket" {
  bucket = "${aws_s3_bucket.app_versioning_bucket.id}"
  policy = <<POLICY
  {
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "eb-ad78f54a-f239-4c90-adda-49e5f56cb51e",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::369554917544:role/aws-elasticbeanstalk-ec2-role"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::elasticbeanstalk-us-east-1-369554917544/resources/environments/logs/*"
        },
        {
            "Sid": "eb-af163bf3-d27b-4712-b795-d1e33e331ca4",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::369554917544:role/aws-elasticbeanstalk-ec2-role"
            },
            "Action": [
                "s3:ListBucket",
                "s3:ListBucketVersions",
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::elasticbeanstalk-us-east-1-369554917544",
                "arn:aws:s3:::elasticbeanstalk-us-east-1-369554917544/resources/environments/*"
            ]
        },
        {
            "Sid": "eb-58950a8c-feb6-11e2-89e0-0800277d041b",
            "Effect": "Deny",
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:DeleteBucket",
            "Resource": "arn:aws:s3:::elasticbeanstalk-us-east-1-369554917544"
        }
    ]
  }
  POLICY
}