package main

import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
	"github.com/aws/aws-sdk-go/service/s3/s3manager"
	"fmt"
	"os"

)

func main() {
	// Create session for batch job.
    sess, err := session.NewSession()
	bucketName := ""
	downloadTarget := ""
	uploadTaget := ""
    localTmpFile := ""

    // Create a downloader with the session and default options
    downloader := s3manager.NewDownloader(sess)

    // Create a file to write the S3 Object contents to.
    downloadContent, err := os.Create(localTmpFile)
    if err != nil {
        fmt.Println(err)
        return
	}

    // Write the contents of S3 Object to the file
    n, err := downloader.Download(downloadContent, &s3.GetObjectInput{
        Bucket: aws.String(bucketName),
        Key:    aws.String(downloadTarget),
    })
    if err != nil {
		fmt.Println(err)
		return
    }
	fmt.Printf("file downloaded, %d bytes\n", n)
	

	// Create an uploader with the session and default options
    uploader := s3manager.NewUploader(sess)

    uploadContent, err  := os.Open(localTmpFile)
    if err != nil {
        fmt.Println(err)
		return
	}

    // Upload the file to S3.
    result, err := uploader.Upload(&s3manager.UploadInput{
        Bucket: aws.String(bucketName),
        Key:    aws.String(uploadTaget),
        Body:   uploadContent,
    })
    if err != nil {
        fmt.Println(err)
		return
    }
    fmt.Printf("file uploaded to, %s\n", result.Location)
}