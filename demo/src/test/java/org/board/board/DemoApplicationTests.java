package org.board.board;

import org.board.board.entity.Question;
import org.board.board.repository.QuestionRepository;
import org.board.board.service.QuestionService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.time.LocalDateTime;

@SpringBootTest
class DemoApplicationTests {

    @Autowired
    private QuestionService questionService;

//    @Test
//    void testJpa() {
//        for (int i = 1; i <= 300; i++) {
//            String subject = String.format("테스트 데이터입니다:[%03d]", i);
//            String content = "내용무";
//            this.questionService.create(subject, content);
//        }
//    }

//    @Test
//    void testJpa() {
//        Question q1 = new Question();
//        q1.setSubject("board가 무엇인가요?");
//        q1.setContent("board에 대해서 알고 싶습니다.");
//        q1.setCreateDate(LocalDateTime.now());
//        this.questionRepository.save(q1);
//
//        Question q2 = new Question();
//        q2.setSubject("board가 무엇인가요?");
//        q2.setContent("board에 대해서 알고 싶습니다.");
//        q2.setCreateDate(LocalDateTime.now());
//        this.questionRepository.save(q2);
//    }

}
