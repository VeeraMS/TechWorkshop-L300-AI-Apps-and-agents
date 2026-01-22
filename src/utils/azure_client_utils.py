"""Utilities for creating Azure OpenAI clients with Managed Identity support."""
import os
from typing import Optional
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider


def create_azure_openai_client(
    endpoint: str,
    api_version: str,
    api_key: Optional[str] = None
) -> AzureOpenAI:
    """
    Create an Azure OpenAI client with automatic fallback to Managed Identity.
    
    Args:
        endpoint: Azure OpenAI endpoint URL
        api_version: API version to use
        api_key: Optional API key. If not provided or empty, uses Managed Identity.
    
    Returns:
        AzureOpenAI client instance
    """
    # Check if api_key is provided and not empty
    if api_key and api_key.strip():
        # Use API key authentication
        return AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key,
            api_version=api_version,
        )
    else:
        # Use Managed Identity / Entra ID authentication
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(),
            "https://cognitiveservices.azure.com/.default"
        )
        return AzureOpenAI(
            azure_endpoint=endpoint,
            azure_ad_token_provider=token_provider,
            api_version=api_version,
        )
