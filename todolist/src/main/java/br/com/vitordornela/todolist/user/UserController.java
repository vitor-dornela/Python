package br.com.vitordornela.todolist.user;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired //injeta a instancia da interface na 'UserController'
    private IUserRepository userRepository;
    @PostMapping("/")
    /*@RequestBody automaticamente converte o conteúdo do corpo da requisição HTTP em um objeto java */
    public UserModel create(@RequestBody UserModel userModel) {
        //System.out.println(userModel.getUsername()); //printar do APIDOG
        var userCreated = this.userRepository.save(userModel);
        return userCreated;
    }
    
}
