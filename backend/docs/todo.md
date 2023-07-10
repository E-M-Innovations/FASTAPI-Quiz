## TODO

1. - [x] Structure Project 
1. - [x] Setup Docker 
1. - [x] Setup MongoDB, create schema, create Database[quizdb] and collections [admin, quizs]
1. - [x] Health Endpoint `/health`    
3. - [x] Add quiz to database `/api/v1/quiz`   
3. - [x] Get quiz my ID `/api/v1/quiz/64aafb154de57c5784084e5d`   
5. - [x] Create Admin Endpoint `/api/v1/admin`     
4. - [x] Get all quiz `/api/v1/quiz?limit=10` default limit 10 -> this endpoint will be called on home page/ quiz pages it will list all available quizzes
7. - [ ] Search by category/theme of quiz   
7. - [ ] Search by quiz name  
6. - [ ] Add authentication for admin so that only authorised person can add quiz.  
7. - [ ] Use JWT to implement cookie based login   
7. - [ ] Delete quiz   
8. - [ ] Think about a secure way to load answer of the quizzes, Option 1 -> Server Side rendering, we will make api call on the frontend using SSR so that api call won't be visible to anyone.  