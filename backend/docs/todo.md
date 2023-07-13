## TODO

1. - [x] Structure Project
1. - [x] Setup Docker
1. - [x] Setup MongoDB, create schema, create Database[quizdb] and collections [admin, quiz]
1. - [x] Health Endpoint `/health`
1. - [x] Add quiz to database `/api/v1/quiz`
1. - [x] Get quiz by ID `/api/v1/quiz/64aafb154de57c5784084e5d`
1. - [x] Create Admin Endpoint `/api/v1/admin`
1. - [x] WhoAMi endpoint `/api/v1/admin/me`
1. - [x] Get all quiz `/api/v1/quiz?limit=10` default limit 10 -> this endpoint will be called on home page/ quiz pages it will list all available quizzes
1. - [x] Search by category/theme of quiz
1. - [x] Search by quiz name
1. - [x] Default admin account creation.
1. - [x] Add authentication for admin so that only authorised person can add quiz.
1. - [x] Authentication endpoint `/api/v1/auth/admin`. -> Send It as formdata {username : "your@email.com","password" : "123"}
1. - [x] Use JWT to implement cookie based login
1. - [x] Only admin can Delete quiz
1. - [x] Only admin can add a quiz
1. - [x] Only admin can add another admin
1. - [x] Activate or deactivate Quiz [only admin]
1. - [ ] Think about a secure way to load answer of the quizzes, Option 1 -> Server Side rendering, we will make api call on the frontend using SSR so that api call won't be visible to anyone.
