# DnD Data

A place to store and retrieve commonly used data for dungeons and dragons.

## Purpose

This webapps purpose is to host data related to Dungeons and Dragaons (like spells, monsters, and other entities) in a singular location with easy callbacks. It's supposed to be a quick reference to this information stored in your own self-hosted data systems.

## Getting Started

The docker container for this project is located [on docker hub](https://hub.docker.com/repository/docker/zachmyers3/dnd-data).

## Developing

To get stared developing pull the repository and set up both `frontend` and `backend` systems.

### Frontend

The frontend is a VueJS application that uses `npm` to manage packages.

```bash
# install packages
$ npm install
# run local test page
$ npm run serve
# test local build before pushing
$ npm run build
```

### Backend

The backend uses FastAPI and uses `poetry` to manage packages.

```bash
# install depenedencies
$ poetry install
# run backend api through uvicorn cli
$ ./backend/scripts/run.sh
```
