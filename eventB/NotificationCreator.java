
public abstract class NotificationCreator {
    public abstract Notification createNotification();

    public void notifyUser() {
        Notification n = createNotification();
        n.send();
    }
}