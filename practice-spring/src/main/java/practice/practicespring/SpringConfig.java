package practice.practicespring;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import practice.practicespring.repository.MemberRepository;
import practice.practicespring.repository.MemoryMemberRepository;
import practice.practicespring.service.MemberService;

@Configuration
public class SpringConfig {

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }
}
