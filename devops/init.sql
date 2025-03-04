-- 테스트 사용자에게 모든 데이터베이스 권한 부여
GRANT ALL PRIVILEGES ON *.* TO 'test'@'%';
FLUSH PRIVILEGES;

-- 메인 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS main;
GRANT ALL PRIVILEGES ON main.* TO 'test'@'%';
FLUSH PRIVILEGES; 

-- 테스트 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS test;
GRANT ALL PRIVILEGES ON test.* TO 'test'@'%';
FLUSH PRIVILEGES; 
