
public class SMSNotification implements Notification {
    private final String number;

    public SMSNotification(String number) {
        this.number = number;
    }

    @Override
    public void send() {
        System.out.println("Sending SMS to " + phoneNumber);
    }
}