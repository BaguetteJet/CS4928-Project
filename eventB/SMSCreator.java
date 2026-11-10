
public class SMSCreator extends NotificationCreator {
    @Override
    public Notification createNotification() {
        return new SMSNotification("1234567");
    }
}