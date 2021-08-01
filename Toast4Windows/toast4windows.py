from winrt.windows.ui.notifications import ToastNotificationManager, ToastNotification
import winrt.windows.data.xml.dom as dom

def custom_notification(title, msg,  app_id, duration='short', icon_link=None):
    notifier = ToastNotificationManager.create_toast_notifier(app_id)
    if icon_link:    
        a_string = '''<toast duration="{3}">
    <visual>
        <binding template="ToastImageAndText02">
            <image id="1" src="{0}" />
            <text id="1"><![CDATA[{1}]]></text>
            <text id="2"><![CDATA[{2}]]></text>
        </binding>
    </visual>
    <actions>
        <action activationType="protocol" content="Dismiss" arguments="dismiss"/>
    </actions>
    <audio src="ms-winsoundevent:Notification.Default" loop="false" />
    </toast>
'''
        a_string = a_string.format(icon_link, title, msg, duration)
    else:
        a_string = '''<toast duration="{2}">
    <visual>
        <binding template="ToastImageAndText02">
            <text id="1"><![CDATA[{0}]]></text>
            <text id="2"><![CDATA[{1}]]></text>
        </binding>
    </visual>
    <actions>
        <action activationType="protocol" content="Dismiss" arguments="dismiss"/>
    </actions>
    <audio src="ms-winsoundevent:Notification.Default" loop="false" />
    </toast>
'''    
        a_string = a_string.format(title, msg, duration)    
    xDoc = dom.XmlDocument()
    xDoc.load_xml(a_string)
    notifier.show(ToastNotification(xDoc))