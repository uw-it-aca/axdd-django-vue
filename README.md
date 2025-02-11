# app_name

[![Build Status](https://github.com/uw-it-aca/django-vue/workflows/Build%2C%20Test%20and%20Deploy/badge.svg)](https://github.com/uw-it-aca/django-vue/actions)
[![Coverage Status](https://coveralls.io/repos/github/uw-it-aca/django-vue/badge.svg?branch=main)](https://coveralls.io/github/uw-it-aca/django-vue?branch=main)

This is a template repository used for creating Django-Vue applications. Use this template to create a new project repository.

## System Requirements

- Python (3.10)
- Rancher Desktop (1.12.1)
- Node (20.11.0 LTS)
- Npm (10.2.4)

## Deployment

- Django-Container (2.0.1)
- Vite (3.1.3)

## Development

- Django (4.2)
- Vue (3.2.28)

## Design

- Bootstrap (5.2)
- Bootstrap Icons (1.9.1)

## Testing

- Vitest (0.23.2)
- Vue Test Utils (2.0.2)

## Linting (code quality)
- Pycodestyle (2.8.x)
- ESLint (8.13.x)
- Stylelint (14.7.x)

## Cloning

Clone this template repo as a new repo (command line)

        $ git clone git@github.com:uw-it-aca/django-vue.git <new-repo>

OR.. using the Gihub interface, click on the "Use this template" button. Github will automatically clone this repo and setup everything for you.

## Configuration

After cloning this repo, find and replace the following instances to match your new repo name.

        'django-vue' with <new-repo>

Find and replace the following instance of the new Django app_name.

        'app_name' with <new_app>
        'app_name_vue' with <new_app_vue>

Copy the sample .env file so that your environment can be run.

        $ cp .env.sample .env

Update any .env variables for local development purposes

## Update README

Replace the README.md file with the README_sample.md

        $ mv README_sample.md README.md
        $ git rm README_sample.md

View the new README on your new Github repository page. Your project should be ready to start development after following those additional steps!
