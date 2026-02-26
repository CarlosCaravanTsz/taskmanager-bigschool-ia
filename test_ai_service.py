import unittest
from unittest.mock import patch, MagicMock
from ai_service import create_simple_tasks

class MockTask:
    def __init__(self, description):
        self.description = description

class TestCreateSimpleTasks(unittest.TestCase):
    @patch("ai_service.client")
    def test_returns_error_if_api_key_not_set(self, mock_client):
        mock_client.api_key = None
        task = MockTask("Organizar una conferencia escolar")
        result = create_simple_tasks(task)
        self.assertEqual(
            result,
            ["Error: OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable."]
        )

    @patch("ai_service.client")
    def test_returns_subtasks_from_openai_response(self, mock_client):
        mock_client.api_key = "fake-key"
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message=MagicMock(content="- Subtarea 1\n- Subtarea 2\n- Subtarea 3"))
        ]
        mock_client.chat.completions.create.return_value = mock_response

        task = MockTask("Organizar una conferencia escolar")
        result = create_simple_tasks(task)
        self.assertEqual(result, ["- Subtarea 1", "- Subtarea 2", "- Subtarea 3"])

    @patch("ai_service.client")
    def test_returns_error_on_exception(self, mock_client):
        mock_client.api_key = "fake-key"
        mock_client.chat.completions.create.side_effect = Exception("API error")
        task = MockTask("Organizar una conferencia escolar")
        result = create_simple_tasks(task)
        self.assertEqual(result, ["Error: API error"])

if __name__ == "__main__":
    unittest.main()
