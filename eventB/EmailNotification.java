
public class EmailNotification implements Notification {
    private final String email;

    public EmailNotification(String email) {
        this.email = email;
    }

    @Override
    public void send() {
        System.out.println("Sending email to " + email);
    }
}