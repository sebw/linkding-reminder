# Linkding bookmark reminder

If you use Linkding and want to be reminded to check some links in the future (for example a product that would launch, some progress on a Github repository), you just need to tag a link with something like `remindme`.

Now you just need to run this container on a recurring basis (for example once a month). When run, the container will find links tagged with `remindme` and it will send a summary by email.

## Running the container

This container can be run from a cron job:

```
docker run \
  -e LINKDING_URL=https://linkding.example.org \
  -e LINKDING_TOKEN=your_api_token \
  -e LINKDING_TAG=remindme \
  -e SMTP_USERNAME=user@example.org \
  -e SMTP_SENDER=user@example.org \
  -e SMTP_RECIPIENT=recipient@example.org \
  -e SMTP_PASSWORD=your_email_password \
  -e SMTP_SERVER=smtp.example.com \
  -e SMTP_PORT=587 \
  --name=shaarli-reminder \
  ghcr.io/sebw/linkding-reminder:0.1
```

Anytime you run the container, you will receive the summary by email.

For links that you don't want to get reminded again, edit the bookmark and just remove the tag.

## Building and running the container locally

```
git clone https://github.com/sebw/linkding-reminder.git
cd linkding-reminder
docker build -t linkding-reminder:v0.0.1
```
