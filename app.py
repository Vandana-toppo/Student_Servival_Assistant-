import streamlit as st

st.set_page_config(
    page_title="Student Survival Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Survival Assistant")
st.write("Your all-in-one student productivity assistant")

st.divider()

# Attendance Input
st.header("📊 Attendance Calculator")

total_classes = st.number_input(
    "Total Classes",
    min_value=0,
    step=1
)

attended_classes = st.number_input(
    "Classes Attended",
    min_value=0,
    step=1
)

# Calculate Attendance
attendance = 0

if total_classes > 0 and attended_classes <= total_classes:
    attendance = (attended_classes / total_classes) * 100

elif attended_classes > total_classes:
    st.error("Classes attended cannot be greater than total classes.")

# Dashboard
st.divider()
st.subheader("📈 Student Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Attendance", f"{attendance:.2f}%")

with col2:
    st.metric("Assignments", "0")

with col3:
    st.metric("Tasks", "0")

# Attendance Status
if total_classes > 0 and attended_classes <= total_classes:

    if attendance >= 75:
        st.success("✅ Your attendance is 75% or above.")
    else:
        st.warning("⚠️ Your attendance is below 75%.")

st.divider()

st.subheader("📚 Student Tools")

st.write("""
- 🎓 CGPA / SGPA Calculator
- 📝 Assignment Tracker
- 💰 Expense & Budget Tracker
- 📚 Notes Organizer
- ⏳ Exam Countdown
- ⏱️ Study Timer
- 📅 Study Planner
- 🔔 Smart Reminders
- ✅ To-Do List
- 📈 Student Performance Dashboard
- 🤖 AI Study Assistant
""")
# CGPA / SGPA Calculator
st.divider()

st.header("🎓 CGPA / SGPA Calculator")

num_subjects = st.number_input(
    "Number of Subjects",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

total_credit_points = 0
total_credits = 0

st.subheader("Enter Subject Details")

for i in range(int(num_subjects)):
    col1, col2 = st.columns(2)

    with col1:
        credit = st.number_input(
            f"Subject {i+1} Credit",
            min_value=0.0,
            step=0.5,
            key=f"credit_{i}"
        )

    with col2:
        grade_point = st.number_input(
            f"Subject {i+1} Grade Point",
            min_value=0.0,
            max_value=10.0,
            step=0.5,
            key=f"grade_{i}"
        )

    total_credit_points += credit * grade_point
    total_credits += credit

if total_credits > 0:
    sgpa = total_credit_points / total_credits

    st.success(f"Your SGPA: {sgpa:.2f}")
    # Assignment Tracker
st.divider()

st.header("📝 Assignment Tracker")

assignment_name = st.text_input("Assignment Name")
subject_name = st.text_input("Subject")
due_date = st.date_input("Due Date")

status = st.selectbox(
    "Status",
    ["Pending", "In Progress", "Completed"]
)

if st.button("Add Assignment"):

    if assignment_name and subject_name:
        st.success(
            f"Assignment '{assignment_name}' added successfully!"
        )

        st.write("**Subject:**", subject_name)
        st.write("**Due Date:**", due_date)
        st.write("**Status:**", status)

    else:
        st.warning("Please enter Assignment Name and Subject.")
        # Expense & Budget Tracker
st.divider()

st.header("💰 Expense & Budget Tracker")

budget = st.number_input(
    "Monthly Budget",
    min_value=0.0,
    step=100.0
)

expense_name = st.text_input("Expense Name")

expense_amount = st.number_input(
    "Expense Amount",
    min_value=0.0,
    step=10.0
)

if st.button("Add Expense"):

    if expense_name and expense_amount > 0:

        st.success(f"Expense '{expense_name}' added successfully!")

        remaining = budget - expense_amount

        st.write("**Expense:**", expense_name)
        st.write("**Amount:** ₹", expense_amount)
        st.write("**Remaining Budget:** ₹", remaining)

        if remaining < 0:
            st.warning("⚠️ You have exceeded your budget.")

    else:
        st.warning("Please enter expense name and amount.")
        # --------------------------------------------------
# NOTES ORGANIZER
# --------------------------------------------------

st.divider()

st.header("📚 Notes Organizer")

note_title = st.text_input(
    "Note Title",
    key="notes_note_title"
)

note_subject = st.text_input(
    "Subject",
    key="notes_note_subject"
)

note_content = st.text_area(
    "Write your notes here",
    height=200,
    key="notes_note_content"
)

if st.button(
    "💾 Save Note",
    key="notes_save_button"
):

    if note_title and note_subject and note_content:

        st.success("✅ Note saved successfully!")

        st.subheader(f"📖 {note_title}")

        st.write(
            f"**Subject:** {note_subject}"
        )

        st.write(note_content)

    else:

        st.warning(
            "⚠️ Please fill Note Title, Subject and Notes."
        )
        # --------------------------------------------------
# EXAM COUNTDOWN
# --------------------------------------------------

st.divider()

st.header("⏳ Exam Countdown")

exam_name = st.text_input(
    "Exam Name",
    key="exam_countdown_name"
)

exam_date = st.date_input(
    "Exam Date",
    key="exam_countdown_date"
)

if st.button(
    "📅 Calculate Countdown",
    key="exam_countdown_button"
):

    from datetime import date

    today = date.today()
    days_left = (exam_date - today).days

    if days_left > 0:
        st.success(
            f"🎯 {exam_name} is in {days_left} days!"
        )

    elif days_left == 0:
        st.warning(
            "🔥 Your exam is TODAY!"
        )

    else:
        st.info(
            "This exam date has already passed."
        )
        # --------------------------------------------------
# STUDY TIMER
# --------------------------------------------------

st.divider()

st.header("⏱️ Study Timer")

study_minutes = st.number_input(
    "Study Time (minutes)",
    min_value=1,
    max_value=180,
    value=25,
    step=5,
    key="study_timer_minutes"
)

if st.button(
    "▶️ Start Study Timer",
    key="study_timer_start"
):

    total_seconds = int(study_minutes * 60)

    st.info(
        f"📚 Study session started for {study_minutes} minutes."
    )

    st.write(
        f"⏳ Timer: {study_minutes} minutes"
    )

    st.progress(0)

    st.caption(
        "Focus on your studies and avoid distractions! 💪"
    )
    # --------------------------------------------------
# STUDY PLANNER
# --------------------------------------------------

st.divider()

st.header("📅 Study Planner")

study_date = st.date_input(
    "Study Date",
    key="planner_date"
)

study_subject = st.text_input(
    "Subject",
    key="planner_subject"
)

study_topic = st.text_input(
    "Topic",
    key="planner_topic"
)

study_duration = st.number_input(
    "Study Duration (minutes)",
    min_value=15,
    max_value=300,
    value=60,
    step=15,
    key="planner_duration"
)

if st.button(
    "➕ Add Study Plan",
    key="planner_add_button"
):

    if study_subject and study_topic:

        st.success("✅ Study plan added!")

        st.write("📅 **Date:**", study_date)
        st.write("📚 **Subject:**", study_subject)
        st.write("📖 **Topic:**", study_topic)
        st.write("⏱️ **Duration:**", study_duration, "minutes")

    else:

        st.warning(
            "⚠️ Please enter Subject and Topic."
        )
        # --------------------------------------------------
# SMART REMINDERS
# --------------------------------------------------

st.divider()

st.header("🔔 Smart Reminders")

reminder_title = st.text_input(
    "Reminder Title",
    key="reminder_title"
)

reminder_date = st.date_input(
    "Reminder Date",
    key="reminder_date"
)

reminder_type = st.selectbox(
    "Reminder Type",
    [
        "Assignment",
        "Exam",
        "Study",
        "Project",
        "Other"
    ],
    key="reminder_type"
)

if st.button(
    "🔔 Add Reminder",
    key="add_reminder"
):

    if reminder_title:

        st.success("✅ Reminder added successfully!")

        st.write("**Reminder:**", reminder_title)
        st.write("**Date:**", reminder_date)
        st.write("**Type:**", reminder_type)

    else:

        st.warning("⚠️ Please enter a reminder title.")
        # --------------------------------------------------
# TO-DO LIST
# --------------------------------------------------

st.divider()

st.header("✅ To-Do List")

todo_task = st.text_input(
    "Task",
    key="todo_task"
)

todo_priority = st.selectbox(
    "Priority",
    ["High", "Medium", "Low"],
    key="todo_priority"
)

if st.button(
    "➕ Add Task",
    key="todo_add_task"
):

    if todo_task:

        st.success("✅ Task added successfully!")

        st.write("**Task:**", todo_task)
        st.write("**Priority:**", todo_priority)

    else:

        st.warning("⚠️ Please enter a task.")
        # --------------------------------------------------
# STUDENT PERFORMANCE DASHBOARD
# --------------------------------------------------

st.divider()

st.header("📊 Student Performance Dashboard")

st.subheader("📈 Performance Overview")

# Default values
if "dashboard_attendance" not in st.session_state:
    st.session_state.dashboard_attendance = 0.0

if "dashboard_sgpa" not in st.session_state:
    st.session_state.dashboard_sgpa = 0.0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Attendance",
        f"{st.session_state.dashboard_attendance:.1f}%"
    )

with col2:
    st.metric(
        "SGPA",
        f"{st.session_state.dashboard_sgpa:.2f}"
    )

with col3:
    st.metric(
        "Study Goal",
        "Active"
    )

st.subheader("🎯 Student Performance")

attendance = st.session_state.dashboard_attendance
sgpa_value = st.session_state.dashboard_sgpa

if attendance >= 75 and sgpa_value >= 7:
    st.success(
        "🌟 Good performance! Keep maintaining your consistency."
    )

elif attendance >= 75:
    st.info(
        "📚 Attendance is good. Focus more on improving your SGPA."
    )

elif sgpa_value >= 7:
    st.info(
        "✅ SGPA is good. Try to maintain your attendance above 75%."
    )

else:
    st.warning(
        "⚠️ Focus on both attendance and academic performance."
    )
