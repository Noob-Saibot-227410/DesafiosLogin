import javax.swing.*;

public class TelaLogin extends JFrame {
    private JLabel lblUsuario, lblSenha;
    private JTextField txtUsuario;
    private JPasswordField txtSenha;
    private JButton btnEntrar;

    public TelaLogin() {
        setTitle("Tela de Login");
        setSize(300, 150);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        getContentPane().add(panel);

        panel.setLayout(null);

        lblUsuario = new JLabel("Usuário:");
        lblUsuario.setBounds(10, 10, 80, 25);
        panel.add(lblUsuario);

        txtUsuario = new JTextField(20);
        txtUsuario.setBounds(100, 10, 160, 25);
        panel.add(txtUsuario);

        lblSenha = new JLabel("Senha:");
        lblSenha.setBounds(10, 40, 80, 25);
        panel.add(lblSenha);

        txtSenha = new JPasswordField(20);
        txtSenha.setBounds(100, 40, 160, 25);
        panel.add(txtSenha);

        btnEntrar = new JButton("Entrar");
        btnEntrar.setBounds(100, 80, 80, 25);
        panel.add(btnEntrar);

        setVisible(true);
    }

    public static void main(String[] args) {
        new TelaLogin();
    }
}
